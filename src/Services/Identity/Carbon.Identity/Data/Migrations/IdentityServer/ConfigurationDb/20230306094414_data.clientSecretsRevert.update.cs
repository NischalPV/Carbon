using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Carbon.Identity.Data.Migrations.IdentityServer.ConfigurationDb
{
    /// <inheritdoc />
    public partial class dataclientSecretsRevertupdate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 9, 44, 14, 245, DateTimeKind.Utc).AddTicks(3520));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 9, 44, 14, 245, DateTimeKind.Utc).AddTicks(4080), "carbon@2023" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.UpdateData(
                table: "ApiScopes",
                keyColumn: "Id",
                keyValue: 1,
                column: "Created",
                value: new DateTime(2023, 3, 6, 8, 34, 1, 295, DateTimeKind.Utc).AddTicks(8470));

            migrationBuilder.UpdateData(
                table: "ClientSecrets",
                keyColumn: "Id",
                keyValue: 1,
                columns: new[] { "Created", "Value" },
                values: new object[] { new DateTime(2023, 3, 6, 8, 34, 1, 295, DateTimeKind.Utc).AddTicks(9030), "60344ff688ccdbdac5286c08be8e1faa81d6ecdc236e5d46f8ef145fa9ef752d" });
        }
    }
}
