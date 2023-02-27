// ApplicationDbContext class
// Path: Data/ApplicationDbContext.cs
using Carbon.Identity;
using Carbon.Identity.Data;
using Carbon.Identity.Models;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    protected override void OnModelCreating(ModelBuilder builder)
    {
        builder.HasDefaultSchema(GlobalConstants.DEFAULT_SCHEMA);
        base.OnModelCreating(builder);
        MasterData.SeedUsingMigration(builder);
    }
}